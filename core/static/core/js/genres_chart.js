// This function will run once the DOM is fully loaded.
document.addEventListener('DOMContentLoaded', () => {
    // Find the canvas element in the HTML.
    const canvas = document.getElementById('genresChart');

    // If the canvas element doesn't exist, stop the script.
    if (!canvas) {
        return;
    }

    // Retrieve the genre data from the canvas's data-* attributes.
    // JSON.parse() is used to convert the string back into a JavaScript array.
    const genreLabels = JSON.parse(canvas.dataset.labels);
    const genreData = JSON.parse(canvas.dataset.data);

    // Get the 2D rendering context for the canvas.
    const ctx = canvas.getContext('2d');

    // Create a new Chart.js instance.
    new Chart(ctx, {
        type: 'bar', // A horizontal bar chart is great for rankings
        data: {
            labels: genreLabels,
            datasets: [{
                label: 'Minutes Listened',
                data: genreData,
                backgroundColor: 'rgba(29, 185, 84, 0.7)',
                borderColor: 'rgba(29, 185, 84, 1)',
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y', // This makes the bar chart horizontal
            responsive: true,
            plugins: {
                legend: {
                    display: false // Hide legend for a cleaner look
                },
                title: {
                    display: true,
                    text: 'Estimated Minutes Listened per Genre',
                    color: '#fff',
                    font: {
                        size: 18
                    }
                }
            },
            scales: {
                x: {
                    ticks: { color: '#fff' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' }
                },
                y: {
                    ticks: { color: '#fff' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' }
                }
            }
        }
    });
});
