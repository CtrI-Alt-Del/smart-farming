document.getElementById('file_input').addEventListener('change', function () {
if (this.value) {
    document.getElementById('submit-icon').classList.remove('hidden')
    document.getElementById('submit-icon').classList.add('flex')
} else {  
    document.getElementById('submit-icon').classList.add('hidden')
    document.getElementById('submit-icon').classList.remove('flex')
}
});
