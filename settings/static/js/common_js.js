"use strict";

// Get cookie from its name (used for the csrf token identification for post/patch/delete requests)
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

// Generate table header from an object id and fields
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

// Generate table rows from a set of objects
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