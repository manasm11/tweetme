import RenderUrl from './components/RenderUrl'
import {tweets_url} from './utils/urls'

function App() {
    return ( 
    <>
    HELLO
    <RenderUrl url={tweets_url}/>
    </>
    );
}

export default App;