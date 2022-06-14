// $(Document).ready(function () {
// Project Review save
$("#addForm").submit(function (event) {
  $.ajax({
    data: $(this).serialize(),
    method: $(this).attr("method"),
    dataType: "json",
    url: $(this).attr("action"),
    success: function (res) {
      if (res.bool == true) {
        $(".ajaxRes").html("Review has been saved.");
        $("#reset").trigger("click");

        //     $('#projectTable').DataTable().ajax.reload();
        // } else {
        //     alert(data.message);
        // }

        // create review
        var _html = '<blockquote class="blockquote text-right">';
        _html += "<small>" + res.data.review + "</small>";
        _html += '<footer class="blockquote-footer">' + res.data.user;
        _html += '<cite title="Source Title">';
        for (var i = 1; i <= res.data.content_rating; i++) {
          _html += '<i class="fa fa-star text-warning"></i>';
        }
        for (var i = 1; i <= res.data.usability_rating; i++) {
          _html += '<i class="fa fa-star text-warning"></i>';
        }
        for (var i = 1; i <= res.data.design_rating; i++) {
          _html += '<i class="fa fa-star text-warning"></i>';
        }
        _html += "</cite>";
        _html += "</footer>";
        _html += "</blockquote>";
        _html += "</hr>";

        // prepend review to review section
        $(".review-list").prepend(_html);

        // hide modal
        $("#productReview").modal("hide");


        //hide modal
        $("#modalhide").modal("hide");
      }
    },
  });
  event.preventDefault();
  // return false;
});

// end Review save
// });
