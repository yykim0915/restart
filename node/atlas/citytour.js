var axios = require('axios');
var data = JSON.stringify({
    "collection": "citytour",
    "database": "citytourdb",
    "dataSource": "Cluster0",
    "projection": {
        "_id": 0,
        "시도명": 1,
        "시군구": 1,
        "시군구": 1,
        "시티투어코스명",
        "시티투어탑승장소명",
        "시티투어코스정보"
    }
});

var config = {
    method: 'post',
    url: 'https://data.mongodb-api.com/app/data-noamn/endpoint/data/beta/action/findOne',
    headers: {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'https://data.mongodb-api.com/app/data-lfifm/endpoint/data/v1'
    },
    data : data
};

axios(config)
    .then(function (response) {
        console.log(JSON.stringify(response.data));
    })
    .catch(function (error) {
        console.log(error);
    });
