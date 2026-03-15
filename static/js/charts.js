const ctx = document.getElementById('transactionChart');

new Chart(ctx, {
type: 'line',
data: {
labels: ['Jan','Feb','Mar','Apr','May'],
datasets: [{
label: 'Transactions',
data: [10,15,8,20,25],
borderColor: '#4f46e5',
fill:false
}]
},
options:{
responsive:true
}
});