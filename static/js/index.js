$(Document).ready(function () {
  // Project Review save
  $("#addForm").submit(function (event) {
    $.ajax({
      data: $(this).serialize(),
      method: $(this).attr("method"),
      dataType: "json",
      url: $(this).attr("action"),
      success: function (res) {
        if (res.bool == true) {
          $(".ajaxRes").html("Data has been saved.");
          $("#reset").trigger("click");
          //     $('#addModal').modal('hide');
          //     $('#projectTable').DataTable().ajax.reload();
          // } else {
          //     alert(data.message);
          // }
        }
      },
    });
    event.preventDefault();
    // return false;
  });

  // end Review save
});
