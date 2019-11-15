document.addEventListener('DOMContentLoaded', function() {
    
        let projectselect = document.getElementById('projectselect');
        let newop = new Option("Select", "select", true, true);
        projectselect.add(newop, 0);
        let wpsselect = document.getElementById('workpackageselect');
        let subselect = document.getElementById('subjectselect');

        projectselect.onchange = () => {
            wpsselect.options.length=0;
            wpsselect.options[0]=new Option("Select", "select", true, true);
            subselect.options.length=0;
            subselect.options[0]=new Option("Select", "select", true, true);
            projectid = projectselect.value;
            axios.post('/projectselect', {
                    prid: projectid                
            })
            .then (response => {
                let wpselHTML = '';
                for (let wp of response.data.wps) {
                    // wpselHTML += '<option value="' + wp.id + '">' + wp.name + '</option>';
                    var op = document.createElement("option");
                    op.textContent = wp.name;
                    op.value = wp.id;
                    wpsselect.append(op);
                }

                // wpsselect.innerHTML = wpselHTML;

            });
        }


        workpackageselect.onchange = () => {
            subselect.options.length=0;
            subselect.options[0]=new Option("Select", "select", true, true);
            wpid = wpsselect.value;
            axios.post('/wpselect', {
                    wpid: wpid                
            })
            .then (response => {
                for (let sub of response.data.subs) {
                    var op = document.createElement("option");
                    op.textContent = sub.name;
                    op.value = sub.id;
                    subselect.append(op);
                }

            });
        }
    }
)
;