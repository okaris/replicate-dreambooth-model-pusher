# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md
import os
from cog import BasePredictor, Input, Path


class Predictor(BasePredictor):
    def setup(self):
        return

    def predict(
        self,
        weights: Path = Input(
            description="A ZIP file containing your trained weights.",
        ),
    ) -> Path:
        dirname = os.path.dirname(weights)
        os.rename(weights, os.path.join(dirname, "output.zip"))
        return Path(os.path.join(dirname, "output.zip"))
