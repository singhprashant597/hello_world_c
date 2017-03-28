//signup user
$(document).on('submit', '#form_signup', function() {
    var inputs = $('#form_signup :input');
    var values = {};
    // values['csrfmiddlewaretoken'] = token;
    var fd = new FormData();
    fd.append('csrfmiddlewaretoken', token);
    for(var i=0; i<inputs.length; i++){
        if (inputs[i].type != 'submit') {
            // values[this.name] = $(this).val();
            // console.log(this.name)
            fd.append(inputs[i].name, inputs[i].value);
        }
    }
    console.log(values);
    console.log(fd)
    $.ajax({
        url: '../../home/add_new_user/',
        type: 'POST',
        data: fd,
        processData: false,
        contentType: false,
        success: function(data) {
            console.log("Done");
            console.log(data);
            window.location = '../../';
        }
    });
    return false;
});
//login user
$(document).on('submit', '#form_login', function() {
    var inputs = $('#form_login :input');
    var values = {};
    // values['csrfmiddlewaretoken'] = token;
    var fd = new FormData();
    fd.append('csrfmiddlewaretoken', token);
    for(var i=0; i<inputs.length; i++){
        if (inputs[i].type != 'submit') {
            // values[this.name] = $(this).val();
            // console.log(this.name)
            fd.append(inputs[i].name, inputs[i].value);
        }
    }
    $.ajax({
        url: '../../home/login_user/',
        type: 'POST',
        data: fd,
        processData: false,
        contentType: false,
        success: function(data) {
            console.log("Done");
            window.location = '../../';
        }
    });
    return false;
})