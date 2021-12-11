"use strict";

// Send a success message after creation or the error from API
function sellCreationSuccess(response) {

    if (response.status == 201) {
        alert("The sell has been added to the database.");
    } else {
        alert(`Error ${response.status} ${response.statusText} on API Call`);
    }
}


// Send a success message after partial update or the error from API
function sellUpdateSuccess(response) {

    if (response.status == 204) {
        alert("The sell has been updated to the database.");
    } else {
        alert(`Error ${response.status} ${response.statusText} on API Call`);
    }
}

// Send a success message after listing or the error from API
function sellListingSuccess(response) {

    if (response.status == 200) {
        let all_sells;

        all_sells = JSON.parse(response.request.response);

        let table = document.getElementById('table_sell');

        if (all_sells[0]) {
            let firstSell = Object.keys(all_sells[0].fields);

            generateTableHead(table, firstSell);
            generateTable(table, all_sells);
        }

    } else {
        alert(`Error ${response.status} ${response.statusText} on API Call`);
    }
}

// Send a success message after deletion or the error from API
function sellDeletionSuccess(response) {

    if (response.status == 204) {
        alert("The sell has been deleted from the database.");
    } else {
        alert(`Error ${response.status} ${response.statusText} on API Call`);
    }
}


// Call the API with create request
function submit_add_sell(event) {

    event.preventDefault();

    let body;
    let apiCall;
    let sellProductId;
    let sellQuantity;

    sellProductId = document.getElementById('product_name_add_sell').value;
    sellQuantity = document.getElementById('sell_quantity_field').value;

    if (sellQuantity != "") {
        body = {
            product: sellProductId,
            quantity: sellQuantity,
        };
        apiCall = [api, body];

        postUrl(apiCall, sellCreationSuccess);
    } else {
        alert("Error : Quantity cannot be blank.");
    }

}

// Call the API with partial update request
function submit_update_sell(event) {

    event.preventDefault();

    let body;
    let apiCall;
    let sellProductId;
    let sellQuantity;
    let sellID;

    sellProductId = document.getElementById('product_name_update_sell').value;
    sellQuantity = document.getElementById('sell_quantity_update_field').value;
    sellID = document.getElementById('sell_name_selector_update').value;

    body = {
        product: sellProductId,
        quantity: sellQuantity,
    };
    apiCall = [(api + sellID), body];

    patchUrl(apiCall, sellUpdateSuccess);
}


// Call the API with delete request
function submit_delete_sell(event) {
    event.preventDefault();

    let body;
    let apiCall;
    let sellID;

    sellID = document.getElementById('sell_name_selector_delete').value;

    apiCall = api + sellID;

    deleteUrl(apiCall, sellDeletionSuccess);

}


// Call the API with list request
function list_sells() {
    getUrl(api, sellListingSuccess);
}

// Path of the called sell API
const api = '/sells/';

// List call for sells table update at page loading
list_sells();
