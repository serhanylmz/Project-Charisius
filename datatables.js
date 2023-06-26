<><script src="https://code.jquery.com/jquery-3.5.1.js"></script><script src="https://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js"></script><script>
    $(document).ready(function () {$("#leaderboard").DataTable({
        lengthMenu: [15, 25, 50, 75, 100],
        language: {
            searchPlaceholder: "Papers, architectures, venues"
        },
        columnDefs: [
            { width: "15%", targets: 4 },
            { width: "15%", targets: 5 }
        ]
    })};
    &rbrace;);
</script></>
