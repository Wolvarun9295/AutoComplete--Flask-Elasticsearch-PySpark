$(function () {
    const $source = $('#source');
    const $result = $('#result');

    $source.autocomplete({
        source: function (request, response) {
            $.ajax({
                url: "/ajax_call",
                type: 'POST',
                dataType: 'json',
                data: {
                    'data': request.term
                },
                success: function (html) {
                    var data = html.suggest.auto[0].options
                    var bucket = [];

                    $.each(data, (index, value) => {
                        bucket.push(value.text)
                    });

                    console.log(bucket);
                    response(bucket);
                }
            });
        },
        autoFocus: true,
        minLength: 0,
    });
});