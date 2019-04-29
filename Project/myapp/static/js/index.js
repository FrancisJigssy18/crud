$(document).ready(function() {
    $('#editTodo').click(function(id){
        $.ajax({
            url: '/edit/' + id,
            type: 'POST',
            cache: false,
            success: function() {
                console.log("You're inside edit function");
            },
            error: function() {
                console.log("Error! Pls try again!");
            }
        });
    });
});