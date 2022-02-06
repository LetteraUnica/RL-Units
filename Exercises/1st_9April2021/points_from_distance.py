import torch
from IPython.display import clear_output

class PointsFromDistanceSolver():
    def __init__(self, D, dims=2):
        self.D = torch.tensor(D)
        self.n_points = D.shape[0]
        self.dims = dims

    @staticmethod
    def compute_distance_matrix(points: torch.Tensor):
        n, d = points.shape
        return torch.norm(points - points.view(n, 1, d), dim=2)

    def cost(self, points, D) -> torch.Tensor:
        D_points = self.compute_distance_matrix(points)
        
        return torch.mean((D_points - D)**2)


    def minimize(self, n_epochs):
        p = torch.randn((self.n_points, self.dims), requires_grad=True)

        optimizer = torch.optim.Rprop([p], lr=1e-1)
        
        for i in range(n_epochs):
            optimizer.zero_grad()
            loss = self.cost(p, self.D)
            print("loss: ", loss.item())
            clear_output(wait=True)
            loss.backward()
            optimizer.step()

        return p.detach().numpy(), loss.detach().numpy()