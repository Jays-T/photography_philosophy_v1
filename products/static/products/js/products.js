$('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#upload-text').text(`Image will be set to: ${file.name}`);
});