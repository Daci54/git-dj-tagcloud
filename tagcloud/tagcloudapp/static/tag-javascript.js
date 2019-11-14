document.addEventListener('DOMContentLoaded', function() {
    
        let projectselect = document.getElementById('projectselect');
        let wpsselect = document.getElementById('workpackageselect');

        projectselect.onchange = () => {
            projectid = projectselect.value;
            axios.post('/optionsselect', {
                    id: projectid                
            })
            .then (response => {
                let optionHTML = '';
                for (let wp of response.data.wps) {
                    optionHTML += '<option value="' + wp.id + '">' + wp.name + '</option>';
                }

                wpsselect.innerHTML = optionHTML;

            });
        }
    }
)
;