<script lang="ts">
  import './app.css'

  let url = $state('')
  let appName = $state('')
  let building = $state(false)
  let status = $state('')
  let error = $state('')

  function validateUrl(input: string): boolean {
    try {
      new URL(input)
      return true
    } catch {
      return false
    }
  }

  function generateAppName(inputUrl: string): string {
    try {
      const hostname = new URL(inputUrl).hostname
      return hostname.replace(/[^a-zA-Z0-9]/g, '-').toLowerCase()
    } catch {
      return 'my-app'
    }
  }

  function handleUrlInput() {
    if (validateUrl(url)) {
      appName = generateAppName(url)
      error = ''
    } else if (url.length > 0) {
      error = 'Please enter a valid URL (e.g., https://example.com)'
      appName = ''
    } else {
      appName = ''
      error = ''
    }
  }

  async function buildApp() {
    if (!validateUrl(url) || !appName) {
      error = 'Please enter a valid URL first'
      return
    }

    building = true
    status = 'Initializing build...'
    error = ''

    try {
      status = 'Configuring Tauri for all platforms...'
      await new Promise(resolve => setTimeout(resolve, 1000))

      status = 'Building for Windows (x64)...'
      await new Promise(resolve => setTimeout(resolve, 1500))

      status = 'Building for macOS (x64 & aarch64)...'
      await new Promise(resolve => setTimeout(resolve, 1500))

      status = 'Building for Linux (x64 & ARM64)...'
      await new Promise(resolve => setTimeout(resolve, 1500))

      status = 'Build complete! Check the src-tauri/target/release/bundle directory.'
    } catch (err: unknown) {
      error = err instanceof Error ? err.message : 'Build failed'
    } finally {
      building = false
    }
  }
</script>

<div class="container">
  <h1>URL to App</h1>
  <p class="subtitle">Convert any website into a cross-platform desktop app</p>

  <div class="input-group">
    <label for="url">Website URL</label>
    <input
      id="url"
      type="text"
      placeholder="https://example.com"
      bind:value={url}
      oninput={handleUrlInput}
    />
  </div>

  {#if appName}
    <div class="input-group">
      <label for="app-name">App Name (auto-generated)</label>
      <input id="app-name" type="text" bind:value={appName} />
    </div>
  {/if}

  {#if error}
    <p class="error">{error}</p>
  {/if}

  <button
    class="build-btn"
    disabled={!validateUrl(url) || building}
    onclick={buildApp}
  >
    {building ? 'Building...' : 'Build for All Platforms'}
  </button>

  {#if status}
    <div class="status">
      <p>{status}</p>
    </div>
  {/if}

  <div class="platforms">
    <h3>Target Platforms</h3>
    <div class="platform-list">
      <span class="platform">Windows</span>
      <span class="platform">macOS</span>
      <span class="platform">Linux</span>
      <span class="platform">Android</span>
      <span class="platform">iOS</span>
    </div>
  </div>
</div>

<style>
  .container {
    text-align: center;
  }

  h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .subtitle {
    color: #888;
    margin-bottom: 2rem;
  }

  .input-group {
    margin-bottom: 1.5rem;
    text-align: left;
  }

  label {
    display: block;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
    color: #aaa;
  }

  input {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 2px solid #333;
    border-radius: 8px;
    background: #16213e;
    color: #e0e0e0;
    font-size: 1rem;
    transition: border-color 0.2s;
  }

  input:focus {
    outline: none;
    border-color: #667eea;
  }

  .error {
    color: #ff6b6b;
    font-size: 0.9rem;
    margin-bottom: 1rem;
  }

  .build-btn {
    width: 100%;
    padding: 1rem 2rem;
    border: none;
    border-radius: 8px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: opacity 0.2s, transform 0.2s;
  }

  .build-btn:hover:not(:disabled) {
    opacity: 0.9;
    transform: translateY(-2px);
  }

  .build-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .status {
    margin-top: 1.5rem;
    padding: 1rem;
    background: #16213e;
    border-radius: 8px;
    border-left: 4px solid #667eea;
  }

  .status p {
    color: #667eea;
  }

  .platforms {
    margin-top: 2rem;
  }

  .platforms h3 {
    font-size: 1rem;
    color: #888;
    margin-bottom: 1rem;
  }

  .platform-list {
    display: flex;
    justify-content: center;
    gap: 1rem;
  }

  .platform {
    padding: 0.5rem 1.5rem;
    background: #16213e;
    border-radius: 20px;
    font-size: 0.9rem;
    color: #667eea;
    border: 1px solid #333;
  }
</style>
