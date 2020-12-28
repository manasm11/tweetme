import RenderUrl from './components/RenderUrl'
import {tweets_url} from './utils/urls'

function App() {
    const props = {url:tweets_url}
    return ( 
    <>
    HELLO
    <RenderUrl {...props}/>
    </>
    );
}

export default App;