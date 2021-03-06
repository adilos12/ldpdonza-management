$(document).ready(function () {
    $(document.body).on("click", "td[data-href]", function () {
        window.location.href = this.dataset.href;
    });

    // only bind the function when the document is ready
    $('#inputGroupFile02').on('change', function() {
        //get the file name
        var fileName = $(this).val().replace("C:\\fakepath\\", "");
        //replace the "Choose a file" label
        $(this).next('.custom-file-label').html(fileName);
    });

    $('#getBetalingen').on('click', function () {
            $.ajax({
                type: 'GET',
                url: '/management/betalingen',
                beforeSend: function() {
                    $('#loading').show();
                    $('#loadingModal').modal('show');
                },
                success: function(data) {
                    window.location.href = '/management/betalingen';
                },
                cache: true
            });
        }
    )
});
