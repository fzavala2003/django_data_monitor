/**
 * Chart.js 3+ line chart con datos de la API y validación de items
 */

async function fetchData() {
  try {
    const response = await fetch('/proxy/api/');
    const jsonData = await response.json();
    console.log(jsonData);

    const items = jsonData.data || {};

    const labels = [];
    const dataValues = [];

    Object.values(items).forEach(item => {
      // Validar que existan fecha y comentario
      if (item.fecha && item.comentario) {
        labels.push(item.fecha);
        dataValues.push(item.comentario.length);
      }
    });

    return { labels, dataValues };
  } catch (error) {
    console.error('Error fetching data:', error);
    return { labels: [], dataValues: [] };
  }
}

async function createChart() {
  const { labels, dataValues } = await fetchData();

  const lineConfig = {
    type: 'line',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Longitud de comentarios',
          backgroundColor: '#0694a2',
          borderColor: '#0694a2',
          data: dataValues,
          fill: false,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          display: true,
        },
        tooltip: {
          mode: 'index',
          intersect: false,
        },
      },
      hover: {
        mode: 'nearest',
        intersect: true,
      },
      scales: {
        x: {
          display: true,
          title: {
            display: true,
            text: 'Fecha',
          },
        },
        y: {
          display: true,
          title: {
            display: true,
            text: 'Longitud del comentario',
          },
          beginAtZero: true,
          ticks: {
            stepSize: 1,
          },
        },
      },
    },
  };

  const lineCtx = document.getElementById('line');
  if (lineCtx) {
    window.myLine = new Chart(lineCtx, lineConfig);
  } else {
    console.error('No se encontró el canvas con id="line"');
  }
}

document.addEventListener('DOMContentLoaded', () => {
  createChart();
});
