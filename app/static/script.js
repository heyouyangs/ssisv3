
document.addEventListener('DOMContentLoaded', function () {
    var getStarted = document.getElementById('getStarted');
    var modal = document.getElementById('myModal');
    var span = document.getElementsByClassName('close')[0];

    function showModal() {
        modal.style.display = 'block';
    }

    function closeModal() {
        modal.style.display = 'none';
    }

    getStarted.onclick = showModal;
    span.onclick = closeModal;

    window.onclick = function (event) {
        if (event.target === modal) {
            closeModal();
        }
    }
})


document.addEventListener('DOMContentLoaded', function () {
    var getStarted = document.getElementById('AddStudentModal');
    var modal = document.getElementById('AddStudentModal');
    var span = document.getElementsByClassName('close')[0];

    function showModal() {
        modal.style.display = 'block';
    }

    function closeModal() {
        modal.style.display = 'none';
    }

    getStarted.onclick = showModal;
    span.onclick = closeModal;

    window.onclick = function (event) {
        if (event.target === modal) {
            closeModal();
        }
    }
})










;