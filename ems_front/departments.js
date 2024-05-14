document.addEventListener('DOMContentLoaded', function() {
    var tableBody = document.getElementById('department-table-body');

    // Make AJAX request to fetch department data
    fetch('http://127.0.0.1:8000/dept_det/dept_all/')
        .then(response => response.json())
        .then(data => {
            // Loop through the department data and create table rows
            data.forEach(department => {
                var row = document.createElement('tr');
                row.innerHTML = `
                    <td>${department.dept_id}</td>
                    <td>${department.dep_name}</td>
                    <td>${department.man_id}</td>
                    <td>
                        <button onclick="demote(${department.dept_id})">Demote</button>
                        <button onclick="removeDept(${department.dept_id})">Remove</button>
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
