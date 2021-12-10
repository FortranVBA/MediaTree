"use strict";

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// URL getter function
function getUrl(url, function_onload) {

    axios.get(url[0]).then(function (response) {
        function_onload(response);
    }, function () {
        alert("Request failed");
    });

}

// URL poster function
function postUrl(url, function_onload) {

    const csrftoken = getCookie('csrftoken');
    alert(csrftoken);

    axios.post(url[0], url[1], { headers: { 'X-CSRFToken': csrftoken } }).then(function (response) {
        function_onload(response);
    }, function () {
        alert("Request failed");
    });
}

function createProductAPICall(response) {
    alert(response.status);
}


function submit_add_product(event) {

    event.preventDefault();

    const api = '/products/';
    let body;
    let apiCall;
    let productName;
    let productDescription;

    productName = document.getElementById('product_name_field').value;
    productDescription = document.getElementById('product_description_field').value;

    body = {
        name: productName,
        description: productDescription,
    };
    apiCall = [api, body];

    postUrl(apiCall, postUrl);
}


button_list_product.onclick = function () {
    const api = '/products/';

    let body;
    let apiCall;

    body = {
    };
    apiCall = [api, body];

    getUrl(apiCall, createProductAPICall);

};