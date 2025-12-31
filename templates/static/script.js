function runEngine() {
    const link = document.getElementById('targetLink').value;
    const action = document.getElementById('action').value;
    const term = document.getElementById('terminal');

    if(!link) {
        alert("يرجى إدخال الرابط أولاً!");
        return;
    }

    term.innerHTML += `<div style="color:var(--neon-blue)">> تم إصدار أمر ${action} للرابط: ${link}</div>`;

    fetch('/start', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({link: link, service: action})
    })
    .then(res => res.json())
    .then(data => {
        term.innerHTML += `<div>> استجابة السيرفر: تم الاتصال والعمل جاري... ✅</div>`;
        term.scrollTop = term.scrollHeight;
    })
    .catch(err => {
        term.innerHTML += `<div style="color:red">> خطأ: فشل الاتصال بالسيرفر!</div>`;
    });
}
