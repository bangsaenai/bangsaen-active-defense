import time
from typing import Dict, Any
from core.engine import HilbertKoopmanEngine

class ActiveDefenseRouter:
    """
    Active Defense & Deception Router Layer mapped to Hilbert Space Core.
    """
    def __init__(self, engine: HilbertKoopmanEngine):
        self.engine = engine

    def process_request(self, prompt: str) -> Dict[str, Any]:
        # ส่ง Prompt เข้า Embedder + Hilbert Engine คำนวณจริง
        metrics, _ = self.engine.evaluate(prompt)
        
        print("\n" + "=" * 70)
        print(f"📥 REQUEST PROMPT : '{prompt}'")
        print("-" * 70)
        print(f"📊 DEBUG METRICS (HILBERT SPACE <Phi(x), Phi(y)>_H) :")
        print(f"  • L2 Energy Norm   : {metrics.energy_norm:.4f}")
        print(f"  • Proj Ratio (Kernel): {metrics.proj_ratio:.4f}")
        print(f"  • Hilbert Distance : {metrics.hilbert_distance:.4f}")
        print(f"  • Decision State   : {metrics.state_label}")
        print(f"  • RAM Sanitization : {'✅ 100% WIPED (Zero Remanence)' if metrics.sanitized else 'ℹ️ RETAINED FOR PASS-THROUGH'}")
        print(f"  • Core Latency     : {metrics.execution_time_ms:.4f} ms")
        print("-" * 70)

        # ROUTING LOGIC
        if metrics.state == 0:
            print("🛡️ [ACTION - STATE 0] Direct Drop. Request Blocked.")
            return {"status": 403, "action": "BLOCK", "response": "Forbidden"}

        elif metrics.state == 2:
            print("🎭 [ACTION - STATE X] ACTIVE DECEPTION TRIGGERED!")
            
            tar_pit_delay = 1.2
            print(f"  -> [Tar-Pit] Injecting {tar_pit_delay}s artificial latency...")
            time.sleep(tar_pit_delay)
            
            fake_canary = "sk-live-canary-882194-x"
            deceptive_response = {
                "status": "success",
                "debug_access": "ADMIN_OVERRIDE_GRANTED",
                "canary_token": fake_canary,
                "message": "System check bypassed. Internal admin shell active."
            }
            
            print(f"  -> [Telemetry] Logging attack vector & Canary Token: {fake_canary}")
            return {"status": 200, "action": "DECEPTION", "payload": deceptive_response}

        else:
            print("✅ [ACTION - STATE 1] PASS-THROUGH. Forwarding payload to LLM Model.")
            return {"status": 200, "action": "ALLOW", "payload": "Safe LLM Response"}