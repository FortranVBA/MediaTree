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

function generateTableHead(table, firstObject) {
    let thead = table.createTHead();
    let row = thead.insertRow();

    // Table Id column title
    let th = document.createElement("th");
    let text = document.createTextNode("Id");
    th.appendChild(text);
    row.appendChild(th);

    // Table fields column titles
    for (let key of firstObject) {
        let th = document.createElement("th");
        let text = document.createTextNode(key);
        th.appendChild(text);
        row.appendChild(th);
    }
}

function generateTable(table, data) {
    for (let element of data) {
        let row = table.insertRow();

        // Fill table Id column
        let cell = row.insertCell();
        let text = document.createTextNode(element['pk']);
        cell.appendChild(text);

        // Fill table fields column
        for (let key in element['fields']) {
            let cell = row.insertCell();
            let text = document.createTextNode(element['fields'][key]);
            cell.appendChild(text);
        }
    }
}

// URL getter function
function getUrl(url, function_onload) {

    axios.get(url).then(function (response) {
        function_onload(response);
    }, function (response) {
        alert(`Error on API Call: ${response}`);
    });

}

// URL poster function
function postUrl(url, function_onload) {

    const csrftoken = getCookie('csrftoken');

    axios.post(url[0], url[1], { headers: { 'X-CSRFToken': csrftoken } }).then(function (response) {
        function_onload(response);
    }, function (response) {
        alert(`Error on API Call: ${response}`);
    });
}

// URL patcher function
function patchUrl(url, function_onload) {

    const csrftoken = getCookie('csrftoken');

    axios.patch(url[0], url[1], { headers: { 'X-CSRFToken': csrftoken } }).then(function (response) {
        function_onload(response);
    }, function (response) {
        alert(`Error on API Call: ${response}`);
    });
}

// URL deleter function
function deleteUrl(url, function_onload) {

    const csrftoken = getCookie('csrftoken');

    axios.delete(url, { headers: { 'X-CSRFToken': csrftoken } }).then(function (response) {
        function_onload(response);
    }, function (response) {
        alert(`Error on API Call: ${response}`);
    });

}

function productCreationSuccess(response) {

    if (response.status == 201) {
        alert("The product has been added to the database.");
    } else {
        alert(`Error ${response.status} ${response.statusText} on API Call`);
    }
}

function productUpdateSuccess(response) {

    if (response.status == 204) {
        alert("The product has been updated to the database.");
    } else {
        alert(`Error ${response.status} ${response.statusText} on API Call`);
    }
}

function productListingSuccess(response) {

    if (response.status == 200) {
        let all_products;

        all_products = JSON.parse(response.request.response);

        let table = document.getElementById('table_product');
        let firstProduct = Object.keys(all_products[0].fields);
        generateTableHead(table, firstProduct);
        generateTable(table, all_products);

    } else {
        alert(`Error ${response.status} ${response.statusText} on API Call`);
    }
}

function productDeletionSuccess(response) {

    if (response.status == 204) {
        alert("The product has been deleted from the database.");
    } else {
        alert(`Error ${response.status} ${response.statusText} on API Call`);
    }
}

function submit_add_product(event) {

    event.preventDefault();

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

    postUrl(apiCall, productCreationSuccess);
}

function submit_update_product(event) {

    event.preventDefault();

    let body;
    let apiCall;
    let productName;
    let productDescription;
    let productID;

    productName = document.getElementById('product_update_name_field').value;
    productDescription = document.getElementById('product_update_description_field').value;
    productID = document.getElementById('product_name_selector_update').value;

    body = {
        name: productName,
        description: productDescription,
    };
    apiCall = [(api + productID), body];

    patchUrl(apiCall, productUpdateSuccess);
}


function submit_delete_product(event) {
    event.preventDefault();

    let body;
    let apiCall;
    let productID;

    productID = document.getElementById('product_name_selector_delete').value;

    apiCall = api + productID;

    deleteUrl(apiCall, productDeletionSuccess);

}


function list_products() {
    getUrl(api, productListingSuccess);
}

const api = '/products/';

list_products();
