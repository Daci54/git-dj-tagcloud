document.addEventListener('DOMContentLoaded', function() {
    
        let projectselect = document.getElementById('projectselect');
        let wpsselect = document.getElementById('workpackageselect');
        let subselect = document.getElementById('subjectselect');

        projectselect.onchange = () => {
            projectid = projectselect.value;
            axios.post('/projectselect', {
                    prid: projectid                
            })
            .then (response => {
                let wpselHTML = '';
                for (let wp of response.data.wps) {
                    wpselHTML += '<option value="' + wp.id + '">' + wp.name + '</option>';
                }

                wpsselect.innerHTML = wpselHTML;

            });
        }



        workpackageselect.onchange = () => {
            wpid = wpsselect.value;
            axios.post('/wpselect', {
                    wpid: wpid                
            })
            .then (response => {
                let subselHTML = '';
                for (let sub of response.data.subs) {
                    subselHTML += '<option value="' + sub.id + '">' + sub.name + '</option>';
                }

                subselect.innerHTML = subselHTML;

            });
        }
    }
)
;