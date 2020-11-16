$(document).on("click", ".like", function(event){
    alert('test');
    // var user_name = $("#id_username").text();
    // var place_id = $(this).data("id");
    // $.ajax({
    //   type: "POST",
    //   url: "{% url 'add_good_place' %}",
    //   data: {'place_id': place_id, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
    //   dataType: "json",
    //   success: function(response){
    //       console.log(this.$(".like-img"));
    //     if (response.message == 1) {
    //         this.$(".like-img").attr('src',"{% static 'like.png' %}")
    //     }
    //     else {
    //         this.$(".like-img").attr('src',"{% static 'dislike.png' %}")
    //     }
    //   },
    // });
  });
