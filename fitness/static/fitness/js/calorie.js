
document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('calorieForm');
  if (!form) return;

  const resultBox = document.getElementById('calorieResultBox');
  const bmrEl = document.getElementById('bmrValue');
  const maintainEl = document.getElementById('maintainValue');
  const cutEl = document.getElementById('cutValue');
  const bulkEl = document.getElementById('bulkValue');
  const proteinEl = document.getElementById('proteinValue');

  const activityFactors = {
    '1.2': 'Sedentary (little/no exercise)',
    '1.375': 'Light exercise (1-3 days/week)',
    '1.55': 'Moderate exercise (3-5 days/week)',
    '1.725': 'Heavy exercise (6-7 days/week)',
    '1.9': 'Athlete (2x per day)'
  };

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const gender = document.querySelector('input[name="calGender"]:checked').value;
    const age = parseFloat(document.getElementById('calAge').value);
    const heightCm = parseFloat(document.getElementById('calHeight').value);
    const weightKg = parseFloat(document.getElementById('calWeight').value);
    const activity = parseFloat(document.getElementById('calActivity').value);

    if (!age || !heightCm || !weightKg || !activity) return;

    let bmr;
    if (gender === 'male') {
      bmr = (10 * weightKg) + (6.25 * heightCm) - (5 * age) + 5;
    } else {
      bmr = (10 * weightKg) + (6.25 * heightCm) - (5 * age) - 161;
    }

    const maintenance = Math.round(bmr * activity);
    const cutting = Math.round(maintenance - 500);
    const bulking = Math.round(maintenance + 300);
    const protein = Math.round(weightKg * 2); // grams/day, general strength-training guideline

    bmrEl.textContent = Math.round(bmr).toLocaleString();
    maintainEl.textContent = maintenance.toLocaleString();
    cutEl.textContent = cutting.toLocaleString();
    bulkEl.textContent = bulking.toLocaleString();
    proteinEl.textContent = protein.toLocaleString() + 'g';

    resultBox.classList.add('show');
    resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  });
});
