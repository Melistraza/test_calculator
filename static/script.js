$(document).ready(function() {
    $('#calculateButton').click(function() {
        var firstNumber = $('#firstInput').val();
        var secondNumber = $('#secondInput').val();
        var operation = $('#operationSelect').val();

        var requestData = {
            "first": firstNumber,
            "second": secondNumber,
            "operation": operation
        };

        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/calc',
            data: JSON.stringify(requestData),
            contentType: 'application/json',
            success: function(response) {
                $('#resultLabel').text('Result: ' + response.result);
            },
            error: function() {
                $('#resultLabel').text('Error occurred during calculation.');
            }
        });
    });
});
