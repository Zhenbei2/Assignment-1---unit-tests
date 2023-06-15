var submit_button = document.getElementById("submit");
submit_button.addEventListener("click", function() {
    var input_field = document.getElementById("string");
    var input_string = input_field.value;

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/partition", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var output_field = document.getElementById("output");
            output_field.innerHTML = xhr.responseText;
        }
    };
    var data = JSON.stringify({ "string": input_string });
    xhr.send(data);
});