let ourCanvas = $("#ourChart");

const chartElement = new Chart(ourCanvas, {
    type: 'line',
    data: {
        labels: [],
        datasets: [
            {
                label: 'Данные от датчика №1 в реальном времени',
                data: [],
                backgroundColor: 'rgba(54, 162, 235, 0.4)',
                borderWidth: 1,
                borderRadius: 7,
                borderColor: 'rgba(54, 162, 235, 0.9)'
            }
        ]
    },
    options: {
        animation: {
            duration: 0
        }
    }
});


function getData()
{
    $.ajax({
        url: '/get_data',
        type: 'POST',
        dataType: 'json',
        data: {
            key: '8jdfsd98sdfsd87'
        },
        success: function (data) {
            let labels = [];
            let new_data = [];
            for (let value in data) {
                labels.push(data[value]['dttm']);
                new_data.push(data[value]['some_number']);
            }
            chartElement.data.labels = labels;
            chartElement.data.datasets[0].data = new_data;
            chartElement.update();
        },
        error: function(jqxhr, status, errorMsg) {
            console.log('Ошибка при взаимодействии с сервером: '+errorMsg);
        }
    });
}

// Код, который выполняется после того, как страница загрузилась
$(function() {
    getData();

    let t = setInterval(
        () => {
            getData();
        },
        1 * 1000
    );

});