$(document).ready(function() {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        method: 'GET',
        success: function(data) {
            let name = data.name;
            $('#character').text(name);
        }

    })
})