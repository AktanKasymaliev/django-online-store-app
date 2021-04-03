(function () {
    $( document ).ready(function () {
        var createUser = '/user/register/'
        var btn = $('.btn')
        btn.click(function(e) {
        e.preventDefault()
        var userName = $('#id_username')
        var mail = $('#id_email')
        var pass = $('#id_password')
        var csrfmiddlewaretoken = $('input[name]').val()
            var data = {username: userName.val(), email: mail.val(), password: pass.val(), csrfmiddlewaretoken: csrfmiddlewaretoken}
            $.post(createUser, data, function(d) {
            userName.val('')
            mail.val('')
            pass.val('')
            alert('Please confirm your mail for login')
            })
        })


    })
}) ()