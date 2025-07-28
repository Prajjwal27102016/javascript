const monthYearElement = document.getElementById('monthyear');
const datesElement = document.getElementById('dates');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

if (!monthYearElement || !datesElement || !prevBtn || !nextBtn) {
    console.error("One or more required elements not found.");
}

let currentDate = new Date();

const updateCalendar = () => {
    const currentYear = currentDate.getFullYear();
    const currentMonth = currentDate.getMonth();

    const firstDay = new Date(currentYear, currentMonth, 1);
    const lastDay = new Date(currentYear, currentMonth + 1, 0);
    const totalDays = lastDay.getDate();
    const firstDayIndex = firstDay.getDay();
    const lastDayIndex = lastDay.getDay();

    const monthyearString = currentDate.toLocaleString('default', {
        month: 'long',
        year: 'numeric'
    });
    monthYearElement.textContent = monthyearString;

    let datesHTML = '';

    // Previous month's trailing dates
    for (let i = firstDayIndex; i > 0; i--) {
        const prevDate = new Date(currentYear, currentMonth, -i + 1);
        datesHTML += `<div class="date inactive">${prevDate.getDate()}</div>`;
    }

    // Current month's dates
    for (let i = 1; i <= totalDays; i++) {
        const date = new Date(currentYear, currentMonth, i);
        const isToday = date.toDateString() === new Date().toDateString();
        const activeClass = isToday ? 'active' : '';
        datesHTML += `<div class="date ${activeClass}">${i}</div>`;
    }
