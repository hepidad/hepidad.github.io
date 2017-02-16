<script type="text/javascript">
				  var toggled;
				  $("#link-toc").click(function (event) {
				    event.preventDefault();
				    var sidebar = $("#sidebar");
				    if (!toggled) {
				      sidebar.transition({x: '25rem'});
				      toggled = true;
				    } else {
				      sidebar.transition({x: '-25rem'});
				      toggled = false;
				    }
				  });
</script>
