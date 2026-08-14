
document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('bmiForm');
  if (!form) return;

  const unitToggle = document.querySelectorAll('input[name="bmiUnit"]');
  const metricFields = document.getElementById('metricFields');
  const imperialFields = document.getElementById('imperialFields');
  const resultBox = document.getElementById('bmiResultBox');
  const bmiValueEl = document.getElementById('bmiValue');
  const bmiCategoryEl = document.getElementById('bmiCategory');
  const bmiPointer = document.getElementById('bmiPointer');
  const bmiAdvice = document.getElementById('bmiAdvice');

  unitToggle.forEach(radio => {
    radio.addEventListener('change', function () {
      if (this.value === 'metric') {
        metricFields.classList.remove('d-none');
        imperialFields.classList.add('d-none');
      } else {
        metricFields.classList.add('d-none');
        imperialFields.classList.remove('d-none');
      }
    });
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    const unit = document.querySelector('input[name="bmiUnit"]:checked').value;
    let bmi = 0;

    if (unit === 'metric') {
      const heightCm = parseFloat(document.getElementById('heightCm').value);
      const weightKg = parseFloat(document.getElementById('weightKg').value);
      if (!heightCm || !weightKg) return;
      const heightM = heightCm / 100;
      bmi = weightKg / (heightM * heightM);
    } else {
      const heightFt = parseFloat(document.getElementById('heightFt').value) || 0;
      const heightIn = parseFloat(document.getElementById('heightIn').value) || 0;
      const weightLb = parseFloat(document.getElementById('weightLb').value);
      if (!weightLb || (!heightFt && !heightIn)) return;
      const totalInches = (heightFt * 12) + heightIn;
      bmi = (weightLb / (totalInches * totalInches)) * 703;
    }

    bmi = Math.round(bmi * 10) / 10;
    bmiValueEl.textContent = bmi.toFixed(1);

    let category = '';
    let advice = '';
    let pointerPct = 0;

    if (bmi < 18.5) {
      category = 'Underweight';
      advice = 'Consider a structured muscle-gain program with a calorie surplus and strength training.';
      pointerPct = (bmi / 18.5) * 25;
    } else if (bmi < 25) {
      category = 'Normal Weight';
      advice = 'Great job! Maintain your results with balanced training and nutrition.';
      pointerPct = 25 + ((bmi - 18.5) / (25 - 18.5)) * 25;
    } else if (bmi < 30) {
      category = 'Overweight';
      advice = 'A combination of cardio, strength training, and a slight calorie deficit can help.';
      pointerPct = 50 + ((bmi - 25) / (30 - 25)) * 25;
    } else {
      category = 'Obese';
      advice = 'We recommend consulting a trainer and starting a guided fat-loss program.';
      pointerPct = Math.min(100, 75 + ((bmi - 30) / 10) * 25);
    }

    bmiCategoryEl.textContent = category;
    bmiAdvice.textContent = advice;
    bmiPointer.style.left = Math.min(100, Math.max(0, pointerPct)) + '%';

    resultBox.classList.add('show');
    resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  });
});
