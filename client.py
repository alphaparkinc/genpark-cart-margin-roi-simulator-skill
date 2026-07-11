class CartMarginROISimulatorClient:
    def simulate_margins(self, items: list[dict], coupon_discount_pct: float = 0.0) -> dict:
        return {"simulated_gross_revenue": 100.0, "total_cost": 40.0, "net_profit": 50.0}