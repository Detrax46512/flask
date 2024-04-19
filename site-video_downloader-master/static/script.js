function baixarVideo() {
    var link = document.getElementById("videoLink").value;

    // Verifica se o link é válido
    if (link.trim() === "") {
        alert("Por favor, insira um link válido!");
        return;
    }

    // Requisição AJAX para baixar o vídeo
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/baixar?link=" + encodeURIComponent(link), true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                alert("Download concluído!");
            } else {
                console.error("Erro durante o download:", xhr.statusText);
            }
        }
    };
    xhr.send();
}
