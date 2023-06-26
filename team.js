// Description: JavaScript for team.html
document.querySelectorAll('.team-member img').forEach(img => {
    img.addEventListener('click', function () {
        window.open(this.dataset.url, '_blank');
    });
});
