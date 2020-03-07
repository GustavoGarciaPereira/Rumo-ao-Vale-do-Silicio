jQuery(document).ready(function($) {
	$("#btn-get-simples2").click(function(){
		$.ajax({
			type: 'GET',
			url: $(this).data('ajax-url2'),
			success: function (ajax) {
				/*$("#resultado-get-simples").val(ajax.content.result);*/
				/*for(let i=0;i<10;i++){
					console.log("Teste: ",ajax.content[i])
				}*/
				/*var obj = JSON.parse(ajax.content);
				console.log("Teste: ",obj[0])*/
				console.log("Teste: ",ajax)
			},
			error: function (ajax) {
				alert('Erro: '+ajax.statusText);
			}
		});	
	});
});