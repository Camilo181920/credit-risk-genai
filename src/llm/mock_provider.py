class MockLLM:

    """
    Proveedor local para pruebas
    sin conexión externa.
    """


    def generate(
        self,
        prompt,
    ):

        return """
Executive Summary

The customer presents a HIGH credit risk profile.

Main Risk Factors

- Low savings level
- Existing financial obligations
- Account status indicates increased risk exposure
- High installment ratio

Recommendation

Perform additional credit review before approval.
Consider reducing the requested amount or requesting
additional guarantees.
"""