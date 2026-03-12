import { useState } from 'react'
import './App.css'

const SPLIT_DAYS = {
  ppl: ['push', 'pull', 'legs'],
  upper_lower: ['upper', 'lower'],
  full_body: ['full'],
}

const SPLIT_LABELS = {
  ppl: 'Push / Pull / Legs',
  upper_lower: 'Upper / Lower',
  full_body: 'Full Body',
}

const MUSCLE_EMOJI = {
  chest: '🫁', back: '🔙', lats: '🔙', quads: '🦵',
  hamstrings: '🦵', calves: '🦵', glutes: '🍑',
  shoulders: '💪', biceps: '💪', triceps: '💪',
  'rear delts': '💪', traps: '💪', forearms: '💪',
}

function App() {
  const [form, setForm] = useState({
    goal: 'hypertrophy',
    difficulty: 'intermediate',
    split_type: 'ppl',
    day: 'push',
  })
  const [workout, setWorkout] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleChange = (e) => {
    const { name, value } = e.target
    setForm((prev) => {
      const updated = { ...prev, [name]: value }
      if (name === 'split_type') updated.day = SPLIT_DAYS[value][0]
      return updated
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setWorkout(null)
    try {
      const params = new URLSearchParams(form)
      const res = await fetch(`/workout?${params}`)
      if (!res.ok) {
        const err = await res.json()
        throw new Error(err.detail || 'Something went wrong')
      }
      setWorkout(await res.json())
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page">
      <header className="header">
        <span className="logo-icon">💪</span>
        <div>
          <h1>Workout Generator</h1>
          <p>Personalized workouts powered by ML</p>
        </div>
      </header>

      <main className="main">
        <form onSubmit={handleSubmit} className="form-card">
          <div className="form-grid">
            <div className="form-group">
              <label>Goal</label>
              <select name="goal" value={form.goal} onChange={handleChange}>
                <option value="hypertrophy">🏗️ Hypertrophy</option>
                <option value="strength">⚡ Strength</option>
                <option value="endurance">🏃 Endurance</option>
              </select>
            </div>

            <div className="form-group">
              <label>Experience</label>
              <select name="difficulty" value={form.difficulty} onChange={handleChange}>
                <option value="beginner">🌱 Beginner</option>
                <option value="intermediate">🔥 Intermediate</option>
                <option value="advanced">🏆 Advanced</option>
              </select>
            </div>

            <div className="form-group">
              <label>Split Type</label>
              <select name="split_type" value={form.split_type} onChange={handleChange}>
                {Object.entries(SPLIT_LABELS).map(([val, label]) => (
                  <option key={val} value={val}>{label}</option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label>Day</label>
              <select name="day" value={form.day} onChange={handleChange}>
                {SPLIT_DAYS[form.split_type].map((d) => (
                  <option key={d} value={d}>{d.charAt(0).toUpperCase() + d.slice(1)}</option>
                ))}
              </select>
            </div>
          </div>

          <button type="submit" className="generate-btn" disabled={loading}>
            {loading ? <span className="spinner" /> : '⚡ Generate Workout'}
          </button>
        </form>

        {error && <div className="error-box">⚠️ {error}</div>}

        {workout && (
          <div className="workout-section">
            <div className="workout-header">
              <h2>{workout.day.charAt(0).toUpperCase() + workout.day.slice(1)} Day</h2>
              <div className="tags">
                <span className="tag goal">{workout.goal}</span>
                <span className="tag difficulty">{workout.difficulty}</span>
                <span className="tag split">{workout.split_type.replace('_', ' ')}</span>
              </div>
            </div>

            <div className="exercise-grid">
              {workout.exercises.map((ex, i) => (
                <div key={ex.exercise_id} className="exercise-card">
                  <div className="card-top">
                    <span className="card-number">{String(i + 1).padStart(2, '0')}</span>
                    <span className="muscle-emoji">{MUSCLE_EMOJI[ex.primary_muscle] || '💪'}</span>
                  </div>
                  <h3>{ex.name}</h3>
                  <div className="muscle-tags">
                    <span className="muscle primary">{ex.primary_muscle}</span>
                    {ex.secondary_muscles && ex.secondary_muscles.split(',').map((m) => (
                      <span key={m} className="muscle secondary">{m.trim()}</span>
                    ))}
                  </div>
                  <div className="card-footer">
                    <span className="equipment">🏋️ {ex.equipment}</span>
                    <span className="sets-reps">{ex.sets} × {ex.reps}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>
    </div>
  )
}

export default App
