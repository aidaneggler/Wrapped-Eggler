document.addEventListener("DOMContentLoaded", function () {
    const labelElement = document.getElementById("genre-labels");
    const dataElement = document.getElementById("genre-data");

    if (!labelElement || !dataElement) return;

    const labels = JSON.parse(labelElement.textContent);
    const data = JSON.parse(dataElement.textContent);

    const ctx = document.getElementById('genresChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                label: 'Genre Distribution',
                data: data,
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: '#ffffff'
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            const label = context.label || '';
                            const value = context.parsed || 0;
                            return `${label}: ${value}`;
                        }
                    }
                }
            }
        }
    });
});
