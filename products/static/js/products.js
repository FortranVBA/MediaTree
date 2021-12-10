"use strict";

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

        if (all_products[0]) {
            let firstProduct = Object.keys(all_products[0].fields);

            generateTableHead(table, firstProduct);
            generateTable(table, all_products);
        }

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
