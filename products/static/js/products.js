"use strict";

// Send a success message after creation or the error from API
function productCreationSuccess(response) {

    if (response.status == 201) {
        alert("The product has been added to the database.");
    } else {
        alert(`Error ${response.status} ${response.statusText} on API Call`);
    }
}

// Send a success message after update or the error from API
function productUpdateSuccess(response) {

    if (response.status == 204) {
        alert("The product has been updated to the database.");
    } else {
        alert(`Error ${response.status} ${response.statusText} on API Call`);
    }
}

// Update the products table after listing or the error from API
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

// Send a success message after deletion or the error from API
function productDeletionSuccess(response) {

    if (response.status == 204) {
        alert("The product has been deleted from the database.");
    } else {
        alert(`Error ${response.status} ${response.statusText} on API Call`);
    }
}

// Call the API with create request
function submit_add_product(event) {

    event.preventDefault();

    let body;
    let apiCall;
    let productName;
    let productDescription;

    productName = document.getElementById('product_name_field').value;
    productDescription = document.getElementById('product_description_field').value;

    if (productName != "") {
        body = {
            name: productName,
            description: productDescription,
        };
        apiCall = [api, body];

        postUrl(apiCall, productCreationSuccess);
    } else {
        alert("Error : Product name cannot be blank.");
    }
}

// Call the API with partial update request
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


// Call the API with delete request
function submit_delete_product(event) {
    event.preventDefault();

    let body;
    let apiCall;
    let productID;

    productID = document.getElementById('product_name_selector_delete').value;

    apiCall = api + productID;

    deleteUrl(apiCall, productDeletionSuccess);

}


// Call the API with list request
function list_products() {
    getUrl(api, productListingSuccess);
}

// Path of the called product API
const api = '/products/';

// List call for product table update at page loading
list_products();
