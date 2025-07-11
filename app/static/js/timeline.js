const timeline_api_url = document.getElementById('posts').dataset.api;
// fetch posts for the timeline
fetch(timeline_api_url)
    .then(res => {
        return res.json();
    })
    .then(data => {
        data.timeline_posts.forEach(post => {
            // This single hash is used for BOTH avatars AND profile data
            const gravatarUrl = getGravatarUrl(post.email);
            const markup = `
            <li class='post'>
                <img src="${gravatarUrl}" />
                <div class="text">
                    <div class="meta">
                        <p class='name'>${post.name}</p>
                        <p class='datetime'>${post.created_at}</p>
                    </div>
                    <p class='content'>${post.content}</p>
                </div>
            </li>`;
            document.getElementById('posts').insertAdjacentHTML('beforeend', markup);
        });
    })
    .catch(error => console.log(error));

// send a post request if the form is submitted
const form = document.getElementById('post');

form.addEventListener('submit', function (e) {
    // Prevent default behavior:
    e.preventDefault();
    // Create payload as new FormData object:
    const payload = new FormData(form);
    // Post the payload using Fetch:
    fetch(timeline_api_url, {
        method: 'POST',
        body: payload,
    })
    location.replace(location.href);
})




// Generate Gravatar url
function getGravatarUrl(email) {
    // Step 1: Hash your email address using SHA-256.
    const hashedEmail = CryptoJS.SHA256(email);
    // Step 2: Construct the Gravatar URL.
    const gravatarUrl = `https://www.gravatar.com/avatar/${hashedEmail}`;
    return gravatarUrl;
}
