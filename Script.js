document.getElementById('beneficiaryForm').addEventListener('submit', function(e){
    e.preventDefault();
    fetch('/add_beneficiary', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({
            name: document.getElementById('bname').value,
            age: document.getElementById('bage').value,
            gender: document.getElementById('bgender').value,
            contact: document.getElementById('bcontact').value
        })
    }).then(res=>res.json()).then(data=>alert(data.message));
});

document.getElementById('programForm').addEventListener('submit', function(e){
    e.preventDefault();
    fetch('/add_program', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({
            name: document.getElementById('pname').value,
            description: document.getElementById('pdesc').value
        })
    }).then(res=>res.json()).then(data=>alert(data.message));
});
