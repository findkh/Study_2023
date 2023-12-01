/**
 * 
 */
//     const grid = new tui.Grid({
//      el: document.getElementById('grid'),
//      data: gridData,
//      scrollX: false,
//      scrollY: false,
//      columns: [
//        {
//          header: 'Name',
//          name: 'name'
//        },
//        {
//          header: 'Artist',
//          name: 'artist'
//        },
//        {
//          header: 'Type',
//          name: 'type'
//        },
//        {
//          header: 'Release',
//          name: 'release'
//        },
//        {
//          header: 'Genre',
//          name: 'genre'
//        }
//      ]
//    });
    
    document.addEventListener("DOMContentLoaded", function(){

		$.ajax({
			url : '/getItemList',
			type: "GET",
//            data: JSON.stringify(form),
            contentType: "application/json; charset=utf-8;",
            dataType: "json",
            success: function(data){
                console.log(data)
            },
			
		})
	
	});