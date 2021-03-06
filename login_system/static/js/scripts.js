$("form[name=signup_form]").submit(function (e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/signup/",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            window.location.href = "/dashboard/";
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });
    e.preventDefault();
})

$("form[name=login_form]").submit(function (e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/login/",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            window.location.href = "/dashboard/";
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });
    e.preventDefault();
})

$("form[name=update_user]").submit(function (e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/update/",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            window.location.href = "/dashboard/";
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });
    e.preventDefault();
})

$("form[name=reset_form]").submit(function (e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/reset/",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            window.location.href = "/";
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });
    e.preventDefault();
})