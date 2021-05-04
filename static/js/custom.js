function validateFileType() {
    var fileName = document.getElementById("fileName").value;
    var idxDot = fileName.lastIndexOf(".") + 1;
    var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
    var button_submit = document.getElementById('btn-submit');

    if (extFile == "jpg" || extFile == "jpeg" || extFile == "png") {
        button_submit.disabled = false;
    } else {
        alert("jpg, jpeg, png만 댐");
        document.getElementById('fileName').value = null;
        button_submit.disabled = true;
    }
};

window.addEventListener("pageshow", function(event) {
    var historyTraversal = event.persisted ||
        (typeof window.performance != "undefined" &&
            window.performance.navigation.type === 2);
    if (historyTraversal) {
        window.location.reload();
    }
});
