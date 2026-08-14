
document.addEventListener('DOMContentLoaded', function () {
  const display = document.getElementById('timerDisplay');
  if (!display) return;

  const statusEl = document.getElementById('timerStatus');
  const roundEl = document.getElementById('timerRoundInfo');
  const startBtn = document.getElementById('timerStart');
  const pauseBtn = document.getElementById('timerPause');
  const resetBtn = document.getElementById('timerReset');
  const ringProgress = document.getElementById('ringProgress');

  const workInput = document.getElementById('workSeconds');
  const restInput = document.getElementById('restSeconds');
  const roundsInput = document.getElementById('totalRounds');

  const beep = new (window.AudioContext || window.webkitAudioContext)();

  function playBeep(freq = 880, duration = 150) {
    try {
      const osc = beep.createOscillator();
      const gain = beep.createGain();
      osc.frequency.value = freq;
      osc.connect(gain);
      gain.connect(beep.destination);
      gain.gain.setValueAtTime(0.15, beep.currentTime);
      osc.start();
      osc.stop(beep.currentTime + duration / 1000);
    } catch (err) { /* audio not available, fail silently */ }
  }

  let totalSeconds = 0;
  let currentSeconds = 0;
  let phase = 'work'; // 'work' | 'rest'
  let currentRound = 1;
  let totalRounds = 5;
  let intervalId = null;
  let isRunning = false;
  let isPaused = false;

  const CIRCUMFERENCE = 2 * Math.PI * 120;

  function formatTime(sec) {
    const m = Math.floor(sec / 60).toString().padStart(2, '0');
    const s = Math.floor(sec % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
  }

  function updateRing() {
    if (!ringProgress) return;
    const pct = totalSeconds > 0 ? currentSeconds / totalSeconds : 0;
    const offset = CIRCUMFERENCE * (1 - pct);
    ringProgress.style.strokeDasharray = CIRCUMFERENCE;
    ringProgress.style.strokeDashoffset = offset;
  }

  function updateDisplay() {
    display.textContent = formatTime(currentSeconds);
    statusEl.textContent = phase === 'work' ? 'Work' : 'Rest';
    statusEl.style.color = phase === 'work' ? 'var(--c-red)' : '#2ecc71';
    roundEl.textContent = `Round ${currentRound} / ${totalRounds}`;
    updateRing();
  }

  function resetTimer() {
    clearInterval(intervalId);
    isRunning = false;
    isPaused = false;
    phase = 'work';
    currentRound = 1;
    totalRounds = parseInt(roundsInput.value, 10) || 5;
    totalSeconds = parseInt(workInput.value, 10) || 30;
    currentSeconds = totalSeconds;
    updateDisplay();
    startBtn.disabled = false;
    startBtn.innerHTML = '<i class="fa-solid fa-play"></i> Start';
    pauseBtn.disabled = true;
  }

  function tick() {
    currentSeconds--;
    if (currentSeconds <= 3 && currentSeconds > 0) playBeep(600, 100);

    if (currentSeconds < 0) {
      // Switch phase
      if (phase === 'work') {
        const restSec = parseInt(restInput.value, 10) || 15;
        if (restSec > 0) {
          phase = 'rest';
          totalSeconds = restSec;
          currentSeconds = restSec;
          playBeep(440, 250);
        } else {
          advanceRound();
          return;
        }
      } else {
        advanceRound();
        return;
      }
    }
    updateDisplay();
  }

  function advanceRound() {
    if (currentRound >= totalRounds) {
      playBeep(1000, 500);
      clearInterval(intervalId);
      isRunning = false;
      statusEl.textContent = 'Complete!';
      statusEl.style.color = '#2ecc71';
      display.textContent = '00:00';
      startBtn.disabled = false;
      startBtn.innerHTML = '<i class="fa-solid fa-rotate-right"></i> Restart';
      pauseBtn.disabled = true;
      return;
    }
    currentRound++;
    phase = 'work';
    playBeep(880, 250);
    totalSeconds = parseInt(workInput.value, 10) || 30;
    currentSeconds = totalSeconds;
    updateDisplay();
  }

  startBtn.addEventListener('click', function () {
    if (beep.state === 'suspended') beep.resume();

    if (!isRunning) {
      if (!isPaused) {
        totalRounds = parseInt(roundsInput.value, 10) || 5;
        totalSeconds = parseInt(workInput.value, 10) || 30;
        currentSeconds = totalSeconds;
        currentRound = 1;
        phase = 'work';
      }
      isRunning = true;
      isPaused = false;
      startBtn.disabled = true;
      pauseBtn.disabled = false;
      updateDisplay();
      intervalId = setInterval(tick, 1000);
    }
  });

  pauseBtn.addEventListener('click', function () {
    clearInterval(intervalId);
    isRunning = false;
    isPaused = true;
    startBtn.disabled = false;
    startBtn.innerHTML = '<i class="fa-solid fa-play"></i> Resume';
    pauseBtn.disabled = true;
  });

  resetBtn.addEventListener('click', resetTimer);
  [workInput, restInput, roundsInput].forEach(el => el.addEventListener('change', resetTimer));

  resetTimer();
});
