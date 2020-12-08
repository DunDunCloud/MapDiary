```
<input
  id="pac-input"
  class="controls"
  type="text"
  placeholder="Search Box"
/>
<button onclick="initMap()">클릭</button>
<div id="map" style="height: 85%;"></div>
```

```
$(".like").click(function(){
    var user_name = $("#user-id").data("id");
    if (user_name == null){
        alert("로그인이 필요합니다.");
        window.location.replace("{% url 'login' %}?next={{request.get_full_path|urlencode}}")
        return ;
    };
    var movie_id = $(this).data("id");
    $.ajax({
      type: "POST",
      url: "{% url 'add_wishlist' %}",
      data: {'movie_id': movie_id, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
      dataType: "json",
      success: function(response){
        $("#count").html(response.like_count+"명이 좋아합니다.");
        if (response.message == 1) {
            $(".like-img").attr('src',"{% static 'movieapp/img/like.png' %}")
        }
        else {
            $(".like-img").attr('src',"{% static 'movieapp/img/dislike.png' %}")
        }
      },
      // error: function(response){
        // alert("로그인이 필요합니다.")
        // window.location.replace("{% url 'login' %}?next={{request.get_full_path|urlencode}}")
      // },
    });
  });

```



```
$(document).on("click", ".like", function(event){
        var user_name = $('#id_username').text();
        var place_id = $(this).data("id");
        $.ajax({
          type: "POST",
          url: "{% url 'add_good_place' %}",
          data: {'place_id': place_id, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
          dataType: "json",
          success: function(response){
              console.log(this.$(".like-img"));
            if (response.message == 1) {
                this.$(".like-img").attr('src',"{% static 'like.png' %}")
            }
            else {
                this.$(".like-img").attr('src',"{% static 'dislike.png' %}")
            }
          },
        });
      });
```

| Field          | Type          |
| -------------- | ------------- |
| title          | CharField     |
| place_name     | CharField     |
| description    | CharField     |
| writer         | CharField     |
| lat            | FloatField    |
| lng            | FloatField    |
| published_date | DateTimeField |

