document.addEventListener('DOMContentLoaded', function() {
    var tableBody = document.getElementById('elemployee-table-body');

    // Make AJAX request to fetch department data
    fetch('http://127.0.0.1:8000/emp_details/elemp_all/')
        .then(response => response.json())
        .then(data => {
            // Loop through the department data and create table rows
            data.forEach(employee => {
                var row = document.createElement('tr');
                row.innerHTML = `
                    <td>${employee.emp_id}</td>
                    <td>${employee.emp_name}</td>
                    <td>${employee.dept_id}</td>
                    <td>${employee.date_of_joining}</td>
                    <td>${employee.years_of_exp}</td>
                        <button onclick="demote(${employee.emp_id})">Demote</button>
                        <button onclick="removeDept(${employee.emp_id})">Remove</button>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error fetching department data:', error);
        });

    // Function to handle demotion of department
    window.demote = function(deptId) {
        // Implement demotion logic here
        console.log('Demote department with ID:', deptId);
    }

    // Function to handle removal of department
    window.removeDept = function(deptId) {
        // Implement removal logic here
        console.log('Remove department with ID:', deptId);
    }
});
